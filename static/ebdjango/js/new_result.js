window.onload = function() {
    console.log("welcome to new result");
    id_game_type = document.getElementById("id_game_type");
    var body = document.getElementsByTagName('body')[0];

    function listQ() {
        console.log("wcisniete id_game_type " + id_game_type.value)
        if (id_game_type.value == "Ping Pong") {
            body.style.backgroundImage = 'url(https://previews.123rf.com/images/bakhtiarzein/bakhtiarzein1603/bakhtiarzein160300032/53583939-table-tennis-ping-pong-woman-female-girl-athlete-play-sport-games-cartoon-drawing-illustration-vecto.jpg)';
        }
        if (id_game_type.value == "Snooker") {
            body.style.backgroundImage = 'url(https://teara.govt.nz/files/38477-enz.jpg)';
        }
    }
    id_game_type.onchange = listQ;
}
