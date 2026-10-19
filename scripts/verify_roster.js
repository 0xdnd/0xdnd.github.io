const fs = require('fs');

const html = fs.readFileSync('index.html', 'utf8');

const tableRows = (html.match(/<tr data-category=/g) || []).length;
const activeTableRows = (html.match(/<tr data-category="active/g) || []).length;
const projectCards = (html.match(/class="project-card[^"]*"/g) || []).length;
const topPercent = (html.match(/Top\s+(5|10)%/gi) || []).length;
const rosterCards = (html.match(/class="roster-card"/g) || []).length;
const has50Plus = html.includes('50+') || html.includes('50&#43;');
const hasActiveStat = html.includes('2 Active') && html.includes('Reactor &amp; Kobold');
const has251 = html.includes('251');
const hasSplitHours = /\(\d+h\)/i.test(html) || /\d+h\s+lecture/i.test(html);

const hasWriteupsSection = html.includes('id="writeups"');
const writeupAnchorsCount = (html.match(/href="#writeups"/g) || []).length;
const hasSecureComms06 = html.includes('06 // Secure Comms');
const readmeHasWriteups = fs.readFileSync('README.md', 'utf8').includes('#writeups');

const hasIsraelMoD = html.includes('Israel Ministry of Defense');
const hasMoDWord = /\bMoD\b/.test(html);
const hasITQCollege = html.includes('ITQ College');
const hasCyberSecurityImplementer = html.includes('Cyber Security Implementer');

console.log('--- CURATED VERIFICATION AUDIT ---');
console.log(`Curated Table Rows: ${tableRows}`);
console.log(`Active Live Season Rows in Table: ${activeTableRows}`);
console.log(`Featured Project Cards: ${projectCards}`);
console.log(`Purged Roster Cards Count: ${rosterCards} (Must be 0)`);
console.log(`Gamified Top 5%/10% Rankings: ${topPercent} (Must be 0)`);
console.log(`Contains 251 Targets: ${has251} (Must be false)`);
console.log(`Contains Split Hours: ${hasSplitHours} (Must be false)`);
console.log(`50+ Solved Metric Present: ${has50Plus}`);
console.log(`Active Stat Card Present: ${hasActiveStat}`);
console.log(`Writeups Section Present: ${hasWriteupsSection} (Must be false)`);
console.log(`Writeup Anchors Count: ${writeupAnchorsCount} (Must be 0)`);
console.log(`06 // Secure Comms Label Present: ${hasSecureComms06} (Must be true)`);
console.log(`README.md Contains #writeups: ${readmeHasWriteups} (Must be false)`);
console.log(`Contains "Israel Ministry of Defense": ${hasIsraelMoD} (Must be false)`);
console.log(`Contains "\\bMoD\\b": ${hasMoDWord} (Must be false)`);
console.log(`Contains "ITQ College": ${hasITQCollege} (Must be true)`);
console.log(`Contains "Cyber Security Implementer": ${hasCyberSecurityImplementer} (Must be true)`);

if (projectCards !== 2) {
  console.error('FAIL: Expected exactly 2 project cards.');
  process.exit(1);
}
if (topPercent !== 0) {
  console.error('FAIL: Found gamified Top 5%/10% rankings.');
  process.exit(1);
}
if (has251) {
  console.error('FAIL: Found 251 targets count.');
  process.exit(1);
}
if (hasSplitHours) {
  console.error('FAIL: Found split hours.');
  process.exit(1);
}
if (tableRows !== 8) {
  console.error(`FAIL: Expected 8 curated table rows, got ${tableRows}.`);
  process.exit(1);
}
if (activeTableRows !== 2) {
  console.error(`FAIL: Expected 2 active season machines in table, got ${activeTableRows}.`);
  process.exit(1);
}
if (rosterCards !== 0) {
  console.error(`FAIL: Roster grid was not purged (found ${rosterCards} cards).`);
  process.exit(1);
}
if (hasWriteupsSection) {
  console.error('FAIL: Found id="writeups" section in index.html.');
  process.exit(1);
}
if (writeupAnchorsCount !== 0) {
  console.error(`FAIL: Found ${writeupAnchorsCount} anchors pointing to #writeups.`);
  process.exit(1);
}
if (!hasSecureComms06) {
  console.error('FAIL: Missing "06 // Secure Comms" in index.html.');
  process.exit(1);
}
if (readmeHasWriteups) {
  console.error('FAIL: README.md contains references to #writeups.');
  process.exit(1);
}
if (hasIsraelMoD) {
  console.error('FAIL: Found "Israel Ministry of Defense" in index.html.');
  process.exit(1);
}
if (hasMoDWord) {
  console.error('FAIL: Found "\\bMoD\\b" in index.html.');
  process.exit(1);
}
if (!hasITQCollege) {
  console.error('FAIL: Missing "ITQ College" in index.html.');
  process.exit(1);
}
if (!hasCyberSecurityImplementer) {
  console.error('FAIL: Missing "Cyber Security Implementer" in index.html.');
  process.exit(1);
}

console.log('PASSED ALL INTEGRITY CHECKS WITH ZERO BLOAT.');
