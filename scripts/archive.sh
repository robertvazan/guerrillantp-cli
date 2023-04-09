#!/bin/sh -e
ARCHIVE=GuerrillaNtp.Cli/bin/archive
mkdir -p $ARCHIVE
dotnet run --project GuerrillaNtp.Cli -c Release >$ARCHIVE/output.txt

