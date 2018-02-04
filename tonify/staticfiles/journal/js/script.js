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
            beforeSend: function(xhr) {
                textarea.val('');
                $("#returned").empty();
                $("<p>loading...</p>").appendTo("#returned");
                console.log(text);
            }

        }).done(function(data) {
            $("#returned").empty();
            var songs = data.tracks;
            console.log(songs);
            for (var i = 0; i < songs.length; i++) {
                var div =
                "<div class='container-fluid'> \
                    <div class='col-md-6'> \
                        <a href=" + songs[i].external_urls.spotify + "> \
                            <img src=" + songs[i].album.images[0].url + " class='img-responsive'/> \
                        </a> \
                    </div> \
                    <div class='col-md-6'> \
                        <p>Song: " + songs[i].name + "</p> \
                        <p>Artist: " + songs[i].album.artists[0].name + "</p> \
                        <p>Album: " + songs[i].album.name + "</p> \
                    </div> \
                </div>"
                console.log(div);
                $(div).appendTo("#returned");
            }
            $("<p>hello</p>").appendTo("#returned");


            //$("<p>" + data["queryResult"]["fulfillmentText"] + "</p>").appendTo("#returned");
        });
    });
});
