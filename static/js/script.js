$(function () {
    $('#comment').on('submit', function (event) {
        event.preventDefault();
        const postId = $('#comment').data('postId');
        $('#commentSection').html(loadingTemplate());
        $.post(`/posts/${postId}/comment`, $('#comment').serialize())
            .then(() => {
                $('#commentBox').val('')
                refreshCommentSection();

            }).catch(err => {
            $('#commentSection').html('No comment');
        })
    });

    refreshCommentSection();


});

function listenCommentDeleteClick() {
    $('.commentDelete').each(function (element) {
        $(this).on('click', function (event) {
            const commentId = $(this).data('commentId');
            if (!confirm('Do you want to delete this comment?')) return;
            $.post(`/comment/${commentId}/delete`, $('#comment').serialize())
                .then(() => {
                    $($(this).parents().get(2)).hide(1000, () => {
                        $($(this).parents().get(2)).remove()
                    })
                })
                .catch((err) => {
                    alert(err.message)
                })
        })
    })
}

function refreshCommentSection() {
    const commentSection = $('#commentSection');
    if (commentSection.length) {
        const postId = $(commentSection[0]).data('postId');

        $.get(`/posts/${postId}/comment`)
            .then((d) => {
                console.log(d)
                setTimeout(() => {
                    commentSection[0].innerHTML = commentTemplate(d.comments);
                    listenCommentDeleteClick()
                }, 1000)
            })
            .catch(err => {
                commentSection[0].innerHTML = 'No comments :(';
                alert(err.message);
            })
        ;
    }
}

function commentTemplate(comments) {
    return `
    <div class="list-group">
    ${comments.map(comment => ` <div href="#" class="list-group-item list-group-item-action ">
    <div class="d-flex w-100 justify-content-between">
      <small>${comment.created_at}</small>
    </div>
    <p class="mb-1">${comment.content}</p>
    <small>${comment.user__first_name} ${comment.user__last_name}
    <br/>
     <span>
     ${window.auth.id == comment.user__id ?
        ` <a href="javascript:void(0)" class="commentDelete" data-comment-id=${comment.id}>
Delete
</a> 
` : ''
    }
  </span>
    </small>
    <br/></div>
   `).join('')}
</div>`
}

function loadingTemplate() {
    return `
      <div class="spinner-border" role="status">
            <span class="sr-only">Loading...</span>
        </div>
`;
}