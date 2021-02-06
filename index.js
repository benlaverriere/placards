const csv = require('csvtojson');
const sqrl = require('squirrelly');
const fs = require('fs');

async function csv2json(inputCSV) {
  return await csv().fromFile(inputCSV);
}

function json2html(inputJSON, templatePath) {
  const template = fs.readFileSync(templatePath, { encoding: 'utf8', flag: 'r' });
  return sqrl.render(template, inputJSON);
}

async function render(inputCSV, templatePath, outputPath) {
  const json = await csv2json(inputCSV);
  const html = json2html(json, templatePath);
  fs.writeFileSync(outputPath, html);
  console.log(`Written to ${outputPath}`);
}

const argv = process.argv.slice(2);
const inputCSV = argv[0];
const template = argv[1];
const outputPath = argv[2];
if (inputCSV == null || inputCSV.length == 0) {
  console.error('Please specify a CSV file to render:\n  generate INPUT_FILE TEMPLATE_FILE OUTPUT_FILE');
} else if (template == null || template.length == 0) {
  console.error('Please specify a template HTML file to use:\n  generate INPUT_FILE TEMPLATE_FILE OUTPUT_FILE');
} else if (outputPath == null || outputPath.length == 0) {
  console.error('Please specify an output HTML file:\n  generate INPUT_FILE TEMPLATE_FILE OUTPUT_FILE');
} else {
  render(inputCSV, template, outputPath);
}
