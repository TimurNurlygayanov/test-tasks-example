How To Run:
-----------

Build index:
```bash
python3 inverted_index.py build --dataset data.txt --output my.index
```

Get results based on text from stdin:
```bash
cat out.txt | python3 inverted_index.py query --index my.index --query-file-cp1251 -
```

Get results based on file:
```bash
python3 inverted_index.py query --index my.index --query-file-utf8 q.txt
```

Get results based on manual query:
```bash
python3 inverted_index.py query --query some --query against --query killing --query then --query and --index my.index
```

Check coverage
```bash
pytest --cov=./ test_inverted_index.py
```