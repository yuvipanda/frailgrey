( function() {

    function showQuote( id ) {
        id = parseInt( id );
        var url = 'data/' + id % 1000 + '/' + id;
        $.get( url ).done( function( data ) {
            $( '#quote' ).text( data );
            setHash( id );
        } );
    }

    function showRandomQuote() {
        var id = Math.random() * 100000;
        showQuote( id );
    }

    function setHash( hash ) {
        window.location.hash = hash;
        $( '#permalink' ).attr( 'href', '#' + hash );
    }

    function getHash() {
        return window.location.hash.substring( 1 );
    }

    $( function() {
        if( getHash() != "" ) {
            showQuote( getHash() );
        } else {
            showRandomQuote();
        }
        $( '#random' ).click( showRandomQuote );
    } );
} )();
