var  licenceButton = document.getElementById('autor');
var  back = document.getElementById('volver');
var  container = document.getElementById('container');

licenceButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

back.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});