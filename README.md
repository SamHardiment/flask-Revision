pipenv install 
pipenv shell


endpoints
- '/' = base.html
- '/pokemon' = 'pokemon/home/template'
- '/pokemon/int:pokemon_id' = json file
-

testing
- pytest --cov-report term-missing --cov=.


step 1:
make seperate api endpoints that can be tested easily


```
/api/pokemon

[{"id":1,"level":12,"name":"Squritle","nickname":"Squritle","type":"Water"},{"id":2,"level":28,"name":"Wartortle","nickname":"Wartortle","type":"Water"},{"id":3,"level":44,"name":"Blastoise","nickname":"Blastoise","type":"Water"}]

passing test
```

```
/api/pokemon/1

{"id":1,"level":12,"name":"Squritle","nickname":"Squritle","type":"Water"}

passing test
```


id issue found in monkeypatch, wartortle and blast' shared the same id, 2


in the pipenv shell, *flask run* to checkout in browser, postman, hoppscotch