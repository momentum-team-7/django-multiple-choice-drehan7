
const deleteButtons = document.querySelectorAll('.delete-button')
for (let button of deleteButtons) {
  button.addEventListener('click', e => {
    const snippetContainer = e.target.parentElement.parentElement;
    const deleteUrl = `/user/snippets/${e.target.id}/delete`;
    fetch (deleteUrl, {
      headers: {

        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
      },
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);
      snippetContainer.remove();
    })
  })
}


document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('pre code').forEach((block) => {
      hljs.highlightBlock(block);
    });
  });