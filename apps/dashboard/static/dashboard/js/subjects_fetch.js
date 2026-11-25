const subjectsContainer = document.querySelector('#subjects-list');

if (subjectsContainer) {
  const status = document.querySelector('#subjects-status');
  const retryButton = document.querySelector('#subjects-retry');
  const subjectTemplate = document.querySelector('#subject-template');

  async function loadSubjects() {
    status.textContent = 'Загружаем направления…';
    retryButton.hidden = true;
    subjectsContainer.hidden = true;

    try {
      const response = await fetch(subjectsContainer.dataset.jsonUrl);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);

      const subjects = await response.json();
      subjectsContainer.replaceChildren();

      if (!Array.isArray(subjects)) throw new Error('Ожидался массив направлений');
      if (subjects.length === 0) {
        status.textContent = 'Направлений пока нет.';
        return;
      }

      subjects.forEach((subject) => {
        const card = subjectTemplate.content.firstElementChild.cloneNode(true);
        card.querySelector('.subject__icon').textContent = subject.icon;
        card.querySelector('.subject__title').textContent = subject.title;
        card.querySelector('.subject__percent').textContent = `${subject.progress}%`;
        card.querySelector('.subject__bar div').style.width = `${subject.progress}%`;
        card.querySelector('.subject__count').textContent = `${subject.completedTopics} из ${subject.totalTopics} тем`;
        subjectsContainer.append(card);
      });

      subjectsContainer.hidden = false;
      status.textContent = '';
    } catch (error) {
      console.error('Не удалось загрузить направления:', error);
      status.textContent = 'Не удалось загрузить направления. Проверьте соединение и повторите попытку.';
      retryButton.hidden = false;
    }
  }

  retryButton.addEventListener('click', loadSubjects);
  loadSubjects();
}
