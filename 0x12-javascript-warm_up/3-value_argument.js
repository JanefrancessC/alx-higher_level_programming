#!/usr/bin/node
const [argc] = process.argv.slice(2);
if (argc === undefined) console.log("No argument");
else console.log(argc);
