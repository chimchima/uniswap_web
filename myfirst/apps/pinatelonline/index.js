function main(arg) {
    var myArgs = process.argv.slice(2);
    console.log(myArgs)
    const fs = require('fs');
    //let tradePrice;
    
    /* 
        Модули для работы:
        "@ethersproject/address": "^5.0.11",
        "@ethersproject/contracts": "^5.0.12",
        "@ethersproject/providers": "^5.0.24",
        "@ethersproject/solidity": "^5.0.10",
        "@uniswap/sdk": "^3.0.3"

    */

    /* 
        Входные данные: 
            1. Адрес контракта меняемого токена
            2. Числа после запятой (Decimals) для меняемого
            3. Сумма меняемого токена
            4. Адрес контакта получаемого токена
            5. Числа после запятой (Decimals) для получаемого

            PS: Адреса контрактов искать на https://etherscan.io/
                Например: https://etherscan.io/address/0xc00e94cb662c3520282e6f5717214004a7f26888
                1. Выбираешь монету поддерживаемую uniswap
                2. Ищешь её в поиске etherscan

        Выходные данные: 
            1. Cумма получаемого токена

    */

    //import { ChainId, Token, Fetcher, Route, Trade, TokenAmount, TradeType  } from '@uniswap/sdk'
    const {ChainId, Token, Fetcher, Route, Trade, TokenAmount, TradeType} = require('@uniswap/sdk');
    //const { async } = require('q');
    const sum = parseInt(myArgs[0]);
    const decimalIn = 18; // число после запятой для меняемого
    const decimalOut = 8; // число после запятой для получаемого

    const tokenIn = new Token(ChainId.MAINNET, '0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2', decimalIn) // тут WBTC и decimal 8 0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599
    const tokenOut = new Token(ChainId.MAINNET, '0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599', decimalOut) // тут WETH и decimal 18 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2
    //const sum = parseInt(fs.readFileSync('in.txt'))//тут сумма меняемого токина
    
    async function init() {
        try {
            
            const pair = await Fetcher.fetchPairData(tokenOut, tokenIn);
            const route = new Route([pair], tokenIn);
            const tokenDecimal = Math.pow(10, decimalIn-1); 
            const trade = new Trade(route, new TokenAmount(tokenIn, tokenDecimal), TradeType.EXACT_INPUT);
            const tradePrice = trade.executionPrice.toSignificant(6)*sum;
            //const tradeNextPrice = trade.nextMidPrice.toSignificant(6)*sum;
            //console.log(sum)
            //console.log(tradePrice);
            //console.log(tradeNextPrice);
            let out = '';
            out +=`${tradePrice.toString()}`;
            //fs.writeFileSync('out.txt', out);
            console.log(out);
            //console.log(tradePrice);
        } catch (ex) {
            console.log('Такого направления для обмена нет');
        }
    }
    init();
   


}

main();