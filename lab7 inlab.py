…
const AddTodo = props => {
let editing = false;
let initialTodoTitle = "";
let initialTodoMemo = "";
if (props.location.state && props.location.state.currentTodo) {
editing = true;
initialTodoTitle = props.location.state.currentTodo.title;
initialTodoMemo = props.location.state.currentTodo.memo;
}
…
const saveTodo = () => {
var data = {
title: title,
memo: memo,
completed: false,
}
if (editing) {
TodoDataService.updateTodo(
props.location.state.currentTodo.id,
data, props.token)
.then(response => {
setSubmitted(true);
console.log(response.data)
})
.catch(e => {
console.log(e);
})
}
else {
TodoDataService.createTodo(data, props.token)
.then(response => {
setSubmitted(true);
})
.catch(e => {
console.log(e);
});
}
}
…