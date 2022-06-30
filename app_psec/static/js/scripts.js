$(function() {
    // layout
    $('#sidebar-toggle').click(function (e) {
        e.preventDefault()
        $('#page').toggleClass('toggled')
    })
    $('#sidebar-toggler-bottom').click(function (e) {
        e.preventDefault()
        $('#page').toggleClass('toggled')
    })

    $('#main-toggle').click(function (e) {
        e.preventDefault()
        $('#header').toggleClass('toggled')
    });

    $('#main-toggle2').click(function (e) {
        e.preventDefault()
        $('#main2').toggleClass('toggled')
    });

    $('#main-toggle2').click(function (e) {
        e.preventDefault()
        $('#main-toggle2').toggleClass('toggled')
    });

    $('#main-toggler-bottom').click(function (e) {
        e.preventDefault()
        $('#header').toggleClass('toggled')
    });
});

