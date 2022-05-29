const keywords = document.querySelectorAll('.keyword-span')

const search = document.getElementById('searchBox')
keywords.forEach((keyword) => {
  keyword.addEventListener('click', (e) => {
    console.log('keyword clicked')
    search.value = e.target.innerText
    search.focus()
    const form = search.closest('form')
    console.log(form)
    form.submit()
  })
})
