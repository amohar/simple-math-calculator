@echo off
java org.antlr.v4.Tool -Dlanguage=Python3 -visitor -no-listener -o .\generated *.g4