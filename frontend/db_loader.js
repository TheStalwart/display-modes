function loadDB() {
  fetch("db.json")
    .then(response => response.json())
    .then(json => buildHTML(json));
}

function buildHTML(db) {
  var gpu_list_container = document.getElementById('gpu-list')

  db.forEach((entry) => {
    console.log(entry)

    var h1 = document.createElement('h1')
    h1.className = `manufacturer_color_${entry.manufacturer}`
    h1.innerText = `[${entry.release_year}] ${entry.manufacturer} ${entry.gpu}`
    gpu_list_container.appendChild(h1)

    var ul_of_modes = document.createElement('ul')

    entry.modes.forEach(mode => {
      var li_of_a_mode = document.createElement('li')

      li_of_a_mode.innerText = `${mode.connector} ${mode.resolution}${mode.hdr ? ' [HDR]' : ''}${mode.vrr ? ' [VRR]' : ''}: ${mode.supported ? '✅' : '❌'}`
      if (mode.notes) {
        li_of_a_mode.innerText = `${li_of_a_mode.innerText} (${mode.notes})`
      }

      ul_of_modes.appendChild(li_of_a_mode)
    });

    gpu_list_container.appendChild(ul_of_modes)
  });
}
