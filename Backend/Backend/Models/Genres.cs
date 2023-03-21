namespace Backend.Models
{
    public class Genres
    {
        public int Id { get; set; }
        public string? Genre { get; set; }
        public string? Color { get; set; }
        public List<Article>? Article { get; set; }




    }
}
