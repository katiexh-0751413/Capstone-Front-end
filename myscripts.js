function filterSort(option){
    let curr_selection = document.getElementById('sort-selection');
    curr_selection.textContent=option;
}

function filterOffice(option){
    let curr_selection = document.getElementById('office-selection');
    curr_selection.textContent=option;
    // ok now tell the python to give me applicants from curr_selection
}

function filterStatus(option){
    let curr_selection = document.getElementById('status-selection');
    curr_selection.textContent=option;
}

function filterJobStat(option){
    let curr_selection = document.getElementById('job-status-selection');
    curr_selection.textContent=option;
}