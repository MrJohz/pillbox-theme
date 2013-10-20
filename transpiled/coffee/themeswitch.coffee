switcher = document.getElementById('theme-switcher-select')
switcher.onchange = () ->
    selectedOption = this.options[this.selectedIndex].value

    pygm = document.getElementById('pygm-theme')
    splits = pygm.href.split('/')
    splits[(splits.length) - 1] = 'pygm-' + selectedOption + '.css'
    pygm.href = splits.join('/')

    main = document.getElementById('main-theme')
    splits = main.href.split('/')
    splits[(splits.length) - 1] = 'main-' + selectedOption + '.css'
    main.href = splits.join('/')

    localStorage.setItem('pillbox-theme', selectedOption)