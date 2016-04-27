var gulp = require('gulp');
var babel = require('babelify');
var browserify = require('browserify');
var browserSync = require('browser-sync');
var buffer = require('vinyl-buffer');
var source = require('vinyl-source-stream');
var sourcemaps = require('gulp-sourcemaps');
var uglify = require('gulp-uglify');
var gulp = require('gulp');
var sass = require('gulp-sass');

var paths = {
  scripts: {
    main: './static/js/app.js',
    files: './static/js/**/*.js',
    dest: './_build/js'
  },
};

var displayError = function(error) {
  // Initial building up of the error
  var errorString = '[' + error.plugin + ']';
  errorString += ' ' + error.message.replace("\n", ''); // Removes new line at the end

  // If the error contains the filename or line number add it to the string
  if (error.fileName)
    errorString += ' in ' + error.fileName;

  if (error.lineNumber)
    errorString += ' on line ' + error.lineNumber;

  // This will output an error like the following:
  // [gulp-sass] error message in file_name on line 1
  console.error(errorString);
};

// Browserify with ES6
gulp.task('scripts', ['scripts:development']);

gulp.task('scripts:development', function() {
  var bundler = browserify(paths.scripts.main, {
    debug: true
  }).transform(babel);

  return bundler.bundle()
    .on('error', function(err) {
      displayError(err);
      this.emit('end');
    })
    .pipe(source('build.js'))
    .pipe(buffer())
    .pipe(sourcemaps.init({
      loadMaps: true
    }))
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest(paths.scripts.dest))
    .pipe(browserSync.reload({stream: true}));
});

gulp.task('scripts:production', function() {
  var bundler = browserify(paths.scripts.main, {
    debug: true
  }).transform(babel);

  return bundler.bundle()
    .on('error', function(err) {
      displayError(err);
    })
    .pipe(source('build.js'))
    .pipe(buffer())
    .pipe(uglify())
    .pipe(gulp.dest(paths.scripts.dest));
});
