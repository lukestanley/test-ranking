module.exports = function (grunt) {
    'use strict';

    grunt.initConfig({

        pkg: grunt.file.readJSON('package.json'),

        // Karma single run
        karma: {
            headless: {
                configFile: 'karma.conf.js'
            },
        },

        // Compile LESS
        less: {
            development: {
                options: {},
                files: {
                    'static/ranking.css': [
                        'src/less/*.less'
                    ]
                }
            }
        },

        // Concat
        concat: {
            options: {
                separator: '; '
            },
            ranker: {
                src: [
                    'src/js/*.js',
                ],
                dest: 'static/ranking.js'
            },
            lib: {
                src: [
                    'node_modules/jquery/dist/jquery.min.js',
                    'node_modules/angular/angular.min.js',
                    'node_modules/bootstrap/dist/js/bootstrap.min.js',
                ],
                dest: 'static/lib.js'
            },
            lib_css: {
                src: [
                    'node_modules/bootstrap/dist/css/bootstrap.min.css',
                ],
                dest: 'static/lib.css'
            },
        },

        // Watch
        watch: {
            styles: {
                files: ['src/less/*.less'],
                tasks: ['less'],
                options: {
                    nospawn: true
                }
            },
            js: {
                files: ['src/js/*.js'],
                tasks: ['concat:ranker'],
                options: {
                    nospawn: true
                }
            }
        }
    });

    // Load plugins
    grunt.loadNpmTasks('grunt-karma');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-concat');

    // Custom tasks
    grunt.registerTask('default', ['watch']);
    grunt.registerTask('build_app', ['less', 'concat:ranker']);
    grunt.registerTask('build_lib', ['concat:lib', 'concat:lib_css']);
};
