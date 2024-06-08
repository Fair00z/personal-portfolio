// function activate
// HTML navigation tabs activate 
function activate(id){
    if (id == 'about'){
        var element = document.getElementById(id)
        element.classList.add('active')
        var services = document.getElementById('services')
        var comments = document.getElementById('comments')
        var home = document.getElementById('home')
        services.classList.remove('active')
        comments.classList.remove('active')
        home.classList.remove('active')
    }
    else if (id == 'services'){
        var element = document.getElementById(id)
        element.classList.add('active')

        var home = document.getElementById('home')
        var about = document.getElementById('about')
        var comments = document.getElementById('comments')

        home.classList.remove('active')
        about.classList.remove('active')
        comments.classList.remove('active')
    }
    else if (id == 'comments'){
        var element = document.getElementById(id)
        element.classList.add('active')

        var home = document.getElementById('home')
        var services = document.getElementById('services')
        var about = document.getElementById('about')

        home.classList.remove('active')
        services.classList.remove('active')
        about.classList.remove('active')
    }
    else{
        var element = document.getElementById(id)
        element.classList.add('active')

        var about = document.getElementById('about')
        var comments = document.getElementById('comments')
        var services = document.getElementById('services')

        about.classList.remove('active')
        comments.classList.remove('active')
        services.classList.remove('active')
    }
}
// function Liked
// liked or disliked
function Liked(option,like_id,dislike_id){
    if (option == 1){
        var LikeIcon = document.getElementById(like_id)
        var DisLikeIcon = document.getElementById(dislike_id)
        console.log(like_id)
        console.log(dislike_id)

        LikeIcon.classList.remove('fa-regular')
        LikeIcon.classList.remove('fa-thumbs-up')
        DisLikeIcon.classList.remove('fa-solid')
        DisLikeIcon.classList.remove('fa-thumbs-down')

        LikeIcon.classList.add('fa-solid')
        LikeIcon.classList.add('fa-thumbs-up')
        DisLikeIcon.classList.add('fa-regular')
        DisLikeIcon.classList.add('fa-thumbs-down')
    }
    else{
        var LikeIcon = document.getElementById(like_id)
        var DisLikeIcon = document.getElementById(dislike_id)

        DisLikeIcon.classList.remove('fa-regular')
        DisLikeIcon.classList.remove('fa-thumbs-down')
        LikeIcon.classList.remove('fa-solid')
        LikeIcon.classList.remove('fa-thumbs-up')

        DisLikeIcon.classList.add('fa-solid')
        DisLikeIcon.classList.add('fa-thumbs-down')
        LikeIcon.classList.add('fa-regular')
        LikeIcon.classList.add('fa-thumbs-up')
    }
}