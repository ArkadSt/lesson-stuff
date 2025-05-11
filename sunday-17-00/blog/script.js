async function loadPosts(){
    let response = await fetch("https://dummyjson.com/posts");
    let data = await response.json();
    console.log(data);

    let posts = data["posts"];
    const slider = document.querySelector('.slider')
    // как создать дивы для каждого поста?
    for(let post of posts){
        
        let slide = document.createElement("div");
        slide.classList.add("slide");

        let img = document.createElement("img");
        img.src = "./photos/4elso4kami.png";
        img.alt = "post image";

        let title = document.createElement("h2"); // <h2></h2>
        title.innerHTML = post["title"];          // <h2>...</h2>

        let metadata = document.createElement("div");
        metadata.id = "metadata";

        let author = document.createElement("div")
        author.id = "author";

        let authorImg = document.createElement("img");
        img.src = "photos/author.png";
        img.alt = "author image";

        // By: Mason Eduard 
        let author_name = document.createElement("p") // <p></p>
        author_name.innerHTML = "By: Mason Eduard"


        let date_and_views = document.createElement("div")
        date_and_views.id = "date_and_views";
        
        let p = document.createElement("p");
        p.innerHTML = `Jan 3, 2022 · ${post["views"]} views`; // ошибка

        author.appendChild(author_name);
        date_and_views.appendChild(p);
        metadata.appendChild(date_and_views);
        metadata.appendChild(author);
        slide.appendChild(img);
        slide.appendChild(h2);
        slide.appendChild(metadata);
 m    }

    // let slide = document.createElement("div")

}

document.addEventListener('DOMContentLoaded', function() {

    loadPosts();

});