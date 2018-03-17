SET OSGEO4W_ROOT=C:\Program Files (x86)\QGIS Valmiera
SET QGIS_PREFIX=%OSGEO4W_ROOT%\apps\qgis
call "%OSGEO4W_ROOT%"\apps\grass\grass-6.4.3\etc\env.bat
SET PATH=%QGIS_PREFIX%\bin;%OSGEO4W_ROOT%\bin;%PATH%
SET PYTHONPATH=%QGIS_PREFIX%\python;%OSGEO4W_ROOT%\apps\Python27;%PYTHONPATH%
SET PYTHONHOME=%OSGEO4W_ROOT%\apps\Python27
python lex.py

pause