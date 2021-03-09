
const deleteButtons = document.querySelectorAll('.delete-button')
for (let button of deleteButtons) {
  button.addEventListener("click", e => {
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

const copyButtons = document.querySelectorAll('.copy-button')
for(let button of copyButtons) {
  button.addEventListener("click", e => {
    const snippetContainer = e.target.parentElement.parentElement;
    const copyURL = `/copy/${e.target.id}/`
    fetch(copyURL, {
      headers: {
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
      },
    })
    .then(response => response.json())
    .then(data => {
      console.log(data)
      if(data['copied'] === 'True') {
        snippetContainer.style.opacity = .6;
        e.target.textContent = "Copied to clipboard & profile!"
        setTimeout(() => {
          snippetContainer.style.opacity = 1;
          e.target.textContent = "Copy";
        }, 2000)

      }
      
    })
  })
}


document.addEventListener('DOMContentLoaded', (event) => {
    document.querySelectorAll('pre code').forEach((block) => {
      hljs.highlightBlock(block);
    });
  });