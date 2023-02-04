pytest -v -m "sanity" --html=Reports\report_sanity.html testCases/ --browser chrome
::pytest -v -m "regression" --html=Reports\report_sanity.html testCases/ --browser chrome
::pytest -v -m "sanity or regression" --html=Reports\report_sanity.html testCases/ --browser chrome
::pytest -v -m "sanity and regression" --html=Reports\report_sanity.html testCases/ --browser chrome

::pytest -v -m "sanity" --html=Reports\report_sanity.html testCases/ --browser firefox
::pytest -v -m "regression" --html=Reports\report_sanity.html testCases/ --browser firefox
::pytest -v -m "sanity or regression" --html=Reports\report_sanity.html testCases/ --browser firefox
::pytest -v -m "sanity and regression" --html=Reports\report_sanity.html testCases/ --browser firefox