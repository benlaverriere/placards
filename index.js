const csv = require('csvtojson');
const json2html_original = require('node-json2html');
const fs = require('fs');

async function csv2json(inputCSV) {
  return await csv().fromFile(inputCSV);
}

function json2html(inputJSON) {
  let template = {'<>':'div','html':'${title} ${year}'};
  return json2html_original.transform(inputJSON, template);
}

async function render(inputCSV) {
  const json = await csv2json(inputCSV);
  const html = json2html(json);
  console.log(html);
}

const argv = process.argv.slice(2);
const inputCSV = argv[0];
if (inputCSV == null || inputCSV.length == 0) {
  console.error('Please specify the input CSV file to render:\n  generate FILE');
} else {
  render(inputCSV);
}
