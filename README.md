# chatgpt-prompt-server

### env
```
python 3.9.13
node 18.16.0
yarn 1.22.19
```

### running locally
First, install `python` `node` and `yarn`.

Second, install python lib:
```
pip install -r requirements.txt
```

Third, install `vercel-cli`:
```
npm i -g vercel
```

Now, use `vercel-cli` to start the server on dev mode:
```
vercel dev
```
And then, the app is now available at http://localhost:3000

### conf
XDG_DATA_HOME
PYPPETEER_HOME