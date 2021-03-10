
const deleteButtons = document.querySelectorAll('.delete-button')
for (let button of deleteButtons) {
  button.addEventListener("click", e => {
    const snippetContainer = e.target.parentElement.parentElement.parentElement;
    const snippetCountLabel = document.querySelector("#snippet-count-label");
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
      var current_count = parseInt(snippetCountLabel.textContent);
      const new_count = current_count -1;
      snippetCountLabel.textContent = new_count;

      

    })
  })
}

const copyButtons = document.querySelectorAll('.copy-button')
for(let button of copyButtons) {
  button.addEventListener("click", e => {
    const snippetContainer = e.target.parentElement.parentElement;
    const totalCount = document.querySelector('#total-copies-label')
    const countLabel = snippetContainer.querySelector('#copies-label')
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

        var currentCount = parseInt(countLabel.textContent);
        countLabel.textContent = currentCount + 1;

        var totalCopies = parseInt(totalCount.textContent);

        totalCount.textContent = totalCopies + 1


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