pytest -s -v -m "sanity" --browser chrome

pytest -s -v -m "sanity or Regression" --browser chrome

pytest -s -v -m "sanity and Regression" --browser chrome

pytest -s -v -m "Regression" --browser chrome