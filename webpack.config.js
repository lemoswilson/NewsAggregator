module.exports = {
    mode: "development",
    entry: {
        main:'./news/static/js/index.js',
        tech:'./news/static/js/tech.js'
    },
    output: {
        filename: '[name].js',
        publicPath: 'http://127.0.0.1:8080/',
    },
    watch: true,
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
        ],
    },
    devServer: {
        headers: {
            'Access-Control-Allow-Origin':'*'
        }
    }
}