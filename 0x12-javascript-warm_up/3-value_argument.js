#!/usr/bin/node
const argc = process.argv.slice(2)
if (argc.length === 0) console.log("No argument")
else console.log(argc[0])
