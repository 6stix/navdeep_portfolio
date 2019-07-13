<DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        @import url('https://fonts.googleapis.com/css?family=Oswald');
    </style>
</head>
<body>

    <?php
    /*
        Nav here, webmaster of the Phoenix of Swarthmore College.

        NOTE: One Phoenix logo uses #AB1616 and another uses #B14635.
    */

    $staticUrl = "http://dev-daily-gazette.pantheon.io/wp-content/themes/colormag/sendout_static/";

    //echo "<a href='https://swarthmorephoenix.com/'><img class='top' src='http://dev-daily-gazette.pantheon.io/wp-content/themes/colormag/sendout_static/phoenixLogo.png' alt='THE PHOENIX'></a>";
    echo "<div class='topper' style='font-family:Arial;font-size:35px;text-align:center;'>The Phoenix</div>";
    echo "<div class='belowTop' style='font-family: Oswald, sans-serif;font-size: 12px;text-align: center;padding-bottom: 25px;'>SWARTHMORE'S INDEPENDENT CAMPUS NEWSPAPER SINCE 1881</div>";

    // Create arrays for each category.
    $news = array();
    $arts = array();
    $opinions = array();
    $sports = array();
    $campusJournal = array();
    $staffEditorials = array();

    // Make a query for posts that are meant for the newsletter. This means posts
    // that are tagged as "newsletter" in Wordpress from the past 24-hours.
    $query = new WP_Query(array('post_type' => "post", 'tag' => "newsletter", 'date_query' => array(
     array(
           'after' => '24 hours ago'
           )
     )));

    // Did the query get any posts?
    if($query->have_posts()){
        // While there still are posts in the query
        while($query->have_posts()){
            // Change the global post variable to the next post in the query
            $query->the_post();
            $currentPermalink = get_permalink();
            $currentTitle = get_the_title();
            $postText = get_the_content();
            $author = get_the_author();

            if (has_category("Arts")) {
                addContentToArray($arts, $currentPermalink, $currentTitle, $postText, $author);
            }

            elseif (has_category("News")){
                addContentToArray($news, $currentPermalink, $currentTitle, $postText, $author);
            }

            elseif (has_category("Sports")){
                addContentToArray($sports, $currentPermalink, $currentTitle, $postText, $author);
            }

            elseif (has_category("Opinion")){
                addContentToArray($opinions, $currentPermalink, $currentTitle, $postText, $author);
            }

            elseif (has_category("Campus Journal")) {
                addContentToArray($campusJournal, $currentPermalink, $currentTitle, $postText, $author);
            }

            elseif (has_category("Staff Editorials")) {
                addContentToArray($staffEditorials, $currentPermalink, $currentTitle, $postText, $author);
            }

            // The following is a mini-testing snippet.
            // if(in_category("please don't work")){
            //     //echo "<br>This shouldn't print.<br>";
            // }
        }

        echo "<div class='articles' style='width: 100%;margin: 0 auto;'>";
        if(empty($news) == false) {
            echo "<div class='categoryDivider' style='width: 100%;margin: 0 auto;'><div class='categoryText' style='font-family: Oswald, sans-serif;font-size: 25px;color: #AB1616;'>News</div><div class='categoryLineBreak'><hr></div></div>";
            popToBeauty($news);
        }

        if(empty($campusJournal) == false) {
            echo "<div class='categoryDivider' style='width: 100%;margin: 0 auto;'><div class='categoryText' style='font-family: Oswald, sans-serif;font-size: 25px;color: #AB1616;'>Campus Journal</div><div class='categoryLineBreak'><hr></div></div>";
            popToBeauty($campusJournal);
        }

        if(empty($staffEditorials) == false) {
            echo "<div class='categoryDivider' style='width: 100%;margin: 0 auto;'><div class='categoryText' style='font-family: Oswald, sans-serif;font-size: 25px;color: #AB1616;'>Staff Editorials</div><div class='categoryLineBreak'><hr></div></div>";
            popToBeauty($staffEditorials);
        }

        if(empty($arts) == false) {
            echo "<div class='categoryDivider' style='width: 100%;margin: 0 auto;'><div class='categoryText' style='font-family: Oswald, sans-serif;font-size: 25px;color: #AB1616;'>Arts</div><div class='categoryLineBreak'><hr></div></div>";
            popToBeauty($arts);
        }

        if(empty($opinions) == false) {
            echo "<div class='categoryDivider' style='width: 100%;margin: 0 auto;'><div class='categoryText' style='font-family: Oswald, sans-serif;font-size: 25px;color: #AB1616;'>Opinions</div><div class='categoryLineBreak'><hr></div></div>";
            popToBeauty($opinions);
        }

        if(empty($sports) == false) {
            echo "<div class='categoryDivider' style='width: 100%;margin: 0 auto;'><div class='categoryText' style='font-family: Oswald, sans-serif;font-size: 25px;color: #AB1616;'>Sports</div><div class='categoryLineBreak'><hr></div></div>";
            popToBeauty($sports);
        }

        echo "</div>";
    }

    else {
        echo "<br>No posts for this newsletter!";
    }

    function addContentToArray(& $array, $currentPermalink, $postText, $author) {
        /* This function adds content to the array that was passed-in by reference. */
        $array[] = $author;
        $array[] = $currentTitle;
        $array[] = $currentPermalink;
        if(strlen($postText) > 200) {
            echo "<div class='readMore'>";
            $readMore = "<a href='".$currentPermalink."'>... Read more.</a>";
            $array[] = substr($postText, 0, 200).$readMore;
            echo "</div>";
        }
        else {
            $array[] = $postText;
        }
    }

    function popToBeauty($array){
        /* This function puts the array of articles into a prettier HTML version. */
        while($array){
            $content = array_pop($array);
            $link = array_pop($array);
            $title = array_pop($array);
            $author = array_pop($array);

            echo "<div class='title' style='text-align: left;color: black;'>";
            echo "<h1 style='font-family: Oswald, sans-serif;font-size: 25px;'><a href='";
            echo $link;
            echo "' style='color: black;text-decoration: none;'>";
            echo $title;
            echo "</a>";
            echo "</div>";

            echo "<div class='articleContent' style='text-align: justify;text-justify: inter-word;font-family: 'Times', sans-serif;'>";
            echo $content;

            echo "<br><div class='author' style='float: right;font-family: Oswald, sans-serif !important;'>- ".$author."</div>";
            echo "</div><br>";
        }
    }
    ?>

</body>
</html>
