const Note = ({ note }) => {
  return (
    <li>
      Name: {note.Title} <br></br>
      Price: {note.Price} <br></br>
      <a href={note.URL} target="_blank">
        <img src={note.Image}></img>
      </a>
    </li>
  );
};

export default Note;
