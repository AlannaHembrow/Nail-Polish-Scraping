import { Link } from "react-router-dom";

export default function Nav() {
  return (
    <div className="navbar">
      <div className="logo">Nail Polish</div>
      <ul className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/about">About</Link>
        <Link to="/favourites">Favourites</Link>
      </ul>
    </div>
  );
}
