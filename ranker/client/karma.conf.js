module.exports = function (config) {
    config.set({
        basePath: '',
        files: [
            'static/lib.js',
            'node_modules/angular-mocks/angular-mocks.js',
            
            'static/ranking.js',
            'test/*.js',
        ],

        frameworks: ['jasmine'],

        reporters: ['mocha'],
        mochaReporter: {
            output: 'autowatch'
        },

        colors: true,

        browsers: ['PhantomJS'],

        singleRun: true,
        autoWatch: false
    });
};