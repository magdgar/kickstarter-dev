/**
 * Created by Tomek on 01.12.2015.
 */

window.addEventListener('WebComponentsReady', function() {
    var app = document.querySelector('#app');

    page('/', function() {
        alert('boo');
        app.route = 'home';
    });

    page('/project', function() {
        app.route = 'project';
    });
});