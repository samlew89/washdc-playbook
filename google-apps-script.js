/**
 * DC Venue Pipeline - Google Apps Script
 *
 * This script provides a REST API for reading/writing venue pipeline data.
 *
 * Setup Instructions:
 * 1. Create a new Google Sheet named "DC Venue Pipeline"
 * 2. Run migrate-to-sheets.py to populate the sheet with venue data
 * 3. Go to Extensions > Apps Script
 * 4. Paste this entire script
 * 5. Click Deploy > New deployment
 * 6. Select "Web app"
 * 7. Set "Execute as" to "Me"
 * 8. Set "Who has access" to "Anyone"
 * 9. Click Deploy and authorize
 * 10. Copy the Web App URL and update APPS_SCRIPT_URL in your HTML files
 */

// Valid pipeline stages
const VALID_STAGES = [
  'Not Started',
  'Contacted',
  'Meeting Set',
  'Negotiating',
  'Installed',
  'Rejected'
];

/**
 * Handle GET requests - returns all venue data as JSON
 */
function doGet(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const data = sheet.getDataRange().getValues();
    const headers = data[0];

    const venues = [];
    for (let i = 1; i < data.length; i++) {
      const row = data[i];
      const venue = {};
      headers.forEach((header, index) => {
        venue[header] = row[index];
      });
      venues.push(venue);
    }

    return ContentService
      .createTextOutput(JSON.stringify({ success: true, venues: venues }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ success: false, error: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * Handle POST requests - updates a venue's stage
 * Expected payload: { venueId: string, stage: string }
 */
function doPost(e) {
  try {
    const payload = JSON.parse(e.postData.contents);
    const { venueId, stage } = payload;

    // Validate stage
    if (!VALID_STAGES.includes(stage)) {
      return ContentService
        .createTextOutput(JSON.stringify({
          success: false,
          error: `Invalid stage. Must be one of: ${VALID_STAGES.join(', ')}`
        }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const data = sheet.getDataRange().getValues();
    const headers = data[0];

    // Find column indices
    const idCol = headers.indexOf('ID');
    const stageCol = headers.indexOf('Stage');
    const lastUpdatedCol = headers.indexOf('LastUpdated');

    if (idCol === -1 || stageCol === -1) {
      return ContentService
        .createTextOutput(JSON.stringify({
          success: false,
          error: 'Sheet missing required columns (ID, Stage)'
        }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    // Find the venue row
    let rowIndex = -1;
    for (let i = 1; i < data.length; i++) {
      if (data[i][idCol] === venueId) {
        rowIndex = i + 1; // +1 because sheets are 1-indexed
        break;
      }
    }

    if (rowIndex === -1) {
      return ContentService
        .createTextOutput(JSON.stringify({
          success: false,
          error: `Venue not found: ${venueId}`
        }))
        .setMimeType(ContentService.MimeType.JSON);
    }

    // Update stage
    sheet.getRange(rowIndex, stageCol + 1).setValue(stage);

    // Update timestamp if column exists
    if (lastUpdatedCol !== -1) {
      const timestamp = new Date().toISOString();
      sheet.getRange(rowIndex, lastUpdatedCol + 1).setValue(timestamp);
    }

    return ContentService
      .createTextOutput(JSON.stringify({
        success: true,
        venueId: venueId,
        stage: stage,
        timestamp: new Date().toISOString()
      }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (error) {
    return ContentService
      .createTextOutput(JSON.stringify({ success: false, error: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}

/**
 * Test function to verify the script is working
 * Run this from the Apps Script editor to check setup
 */
function testScript() {
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  const data = sheet.getDataRange().getValues();
  const headers = data[0];

  Logger.log('Headers: ' + headers.join(', '));
  Logger.log('Total rows: ' + (data.length - 1));

  // Check required columns
  const requiredCols = ['ID', 'Name', 'Stage', 'LastUpdated'];
  const missingCols = requiredCols.filter(col => !headers.includes(col));

  if (missingCols.length > 0) {
    Logger.log('WARNING: Missing columns: ' + missingCols.join(', '));
  } else {
    Logger.log('All required columns present');
  }

  // Count stages
  const stageCol = headers.indexOf('Stage');
  if (stageCol !== -1) {
    const stageCounts = {};
    for (let i = 1; i < data.length; i++) {
      const stage = data[i][stageCol] || 'Not Started';
      stageCounts[stage] = (stageCounts[stage] || 0) + 1;
    }
    Logger.log('Stage counts: ' + JSON.stringify(stageCounts));
  }
}
