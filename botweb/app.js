const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

const porta = 3000;

app.get('/conversa/: texto*?', (req,res)=>{

const {Text} = req.params;
        
        
        res.json(texto);


});

app.listen(porta, () => console.log('Rodando na porta 3000'));

