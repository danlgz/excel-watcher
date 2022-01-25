const $folderStatus = document.querySelector('#folder-status');
const $stopToWatchBtn = document.querySelector('#stop-watch-btn');
const $watchBtn = document.querySelector('#watch-btn');
const $folderSelectorBtn = document.querySelector('#folder-selector-btn');
const $statusProcess = document.querySelector('#status-process');
const notSelectedText = 'Folder not selected';

// helpers
const folderSelected = (path) => {
    $folderStatus.innerHTML = path;
    $folderStatus.parentElement.classList.add('selected');
    $watchBtn.classList.remove('disabled');
}
const folderNotSelected = () => {
    $folderStatus.innerHTML = notSelectedText;
    $folderStatus.parentElement.classList.remove('selected');
    $watchBtn.classList.add('disabled');
}

const watchingFolder = () => {
    $watchBtn.classList.add('hidden');
    $stopToWatchBtn.classList.remove('hidden');
    $folderSelectorBtn.classList.add('disabled');
}

const stopToWatch = () => {
    $watchBtn.classList.remove('hidden');
    $stopToWatchBtn.classList.add('hidden');
    $folderSelectorBtn.classList.remove('disabled');
}

// DOM events
$folderSelectorBtn.addEventListener("click", function () {
    if (this.classList.contains('disabled')) return;
    eel.py_select_folder()();
});

$watchBtn.addEventListener("click", function () {
    if (this.classList.contains('disabled')) return;
    eel.py_start_to_watch()();
    $statusProcess.innerHTML = 'Waiting files...';
});

$stopToWatchBtn.addEventListener("click", function () {
    if (this.classList.contains('disabled')) return;
    eel.py_stop_to_watch()();
    $statusProcess.innerHTML = '';
})

// functions to expose to python
eel.expose(js_reload_dom);
function js_reload_dom() {
    serverData();
}

eel.expose(js_processing_file);
function js_processing_file(file) {
    $statusProcess.innerHTML = `processing: ${file}`;
}

eel.expose(js_queue_done);
function js_queue_done() {
    $statusProcess.innerHTML = 'Done!';
}

// constructor
async function serverData() {
    const {
        folder_path = '',
        is_watching = false,
    } = await eel.py_get_meta()();
    console.log('is_watching', is_watching);

    if (!!folder_path && !Array.isArray(folder_path)) folderSelected(folder_path);
    else folderNotSelected();

    if (is_watching) watchingFolder();
    else stopToWatch();
}
serverData();