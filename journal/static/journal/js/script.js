$(document).ready(function() {

    $("#form-submit").on("submit", function(e) {
        e.preventDefault();

        url = location.protocol + "//" + location.host + "/journal/returnPlaylist"

        var textarea = $('textarea#taskInput');
        var text = textarea.val();
        console.log(text);
        $.ajax({
            type: "POST",
            url: url,
            data: {
                "input": text,
            },
            statusCode: {
                500: function() {
                    $("#returned").empty();
                    $("<p>Oops, looks like there's a server error!</p>").appendTo("#returned");
                }
            },
            beforeSend: function(xhr) {
                textarea.val('');
                $("#returned").empty();
                //$("<p>loading...</p>").appendTo("#returned");
                $("button").text("Loading...");
                console.log(text);
            }

        }).done(function(data) {
            $("#returned").empty();
            $("button").text("Generate Playlist");
            var songs = data.tracks;
            console.log(songs);
            for (var i = 0; i < songs.length; i++) {
                /*
                var div =
                "<div class='container-fluid'> \
                    <div class='col-md-6'> \
                        <a href=" + songs[i].external_urls.spotify + "> \
                            <img src=" + songs[i].album.images[0].url + " class='img-responsive'/> \
                        </a> \
                    </div> \
                    <div class='col-md-6'> \
                        <h3>Song: " + songs[i].name + "</h3> \
                        <h3>Artist: " + songs[i].album.artists[0].name + "</h3> \
                        <h3>Album: " + songs[i].album.name + "</h3> \
                    </div> \
                </div>"
                */
                var div =
                "<div class='col-md-3'> \
                    <a href=" + songs[i].external_urls.spotify + "> \
                        <img src=" + songs[i].album.images[0].url + " class='img-responsive'/> \
                    </a> \
                    <h6>Song: " + songs[i].name + "</h6> \
                    <h6>Artist: " + songs[i].album.artists[0].name + "</h6> \
                    <h6>Album: " + songs[i].album.name + "</h6> \
                </div>";
                console.log(div);
                $(div).appendTo("#returned");
            }

            //$("<p>" + data["queryResult"]["fulfillmentText"] + "</p>").appendTo("#returned");
        });
    });
});
