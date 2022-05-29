const keywords = document.querySelectorAll('.actor-name')

const search = document.getElementById('searchBox')
keywords.forEach((keyword) => {
  keyword.addEventListener('click', (e) => {
    // console.log(e)
    const actor = e.target
    if (!actor) return
    search.value = actor.innerText
    // console.log(search.value)
    search.focus()
    const form = search.closest('form')
    // console.log(form)
    form.submit()
  })
})
