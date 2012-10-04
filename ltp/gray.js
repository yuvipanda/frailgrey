( function() {

    function showQuote( id ) {
        id = parseInt( id );
        var url = 'data/' + id % 1000 + '/' + id;
        $.get( url ).done( function( data ) {
            $( '#quote' ).text( data );
            setHash( id );
            setTweetLink( data );
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

    function setTweetLink( text ) {
        var $twitter = $( '#share-twitter' );
        var tweetText = '"' + text + '"';
        var url = "https://twitter.com/share?text=" + encodeURIComponent( tweetText ) + "&url=" + encodeURIComponent( window.location.href );
        $twitter.attr( 'href', url );
    }

    $( function() {
        if( getHash() != "" ) {
            showQuote( getHash() );
        } else {
            showRandomQuote();
        }
        $( '#random' ).click( showRandomQuote );
        $( document ).keydown( function() {
            if( event.which === 82 ) {
                // r or R
                showRandomQuote();
            } else if( event.which === 84 ) {
                // t
                window.open( $( '#share-twitter' ).attr( 'href' ) );
            }
        } );
    } );
} )();
