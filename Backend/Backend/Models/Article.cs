namespace Backend.Models
{
    public class Article
    {
        public int Id { get; set; }
        public string? Authors { get; set; }
        public int? Year { get; set; }
        public string? Title { get; set; }
        public string? Journal { get; set; }
        public int? Issue { get; set; }
        public string? Place { get; set; }
        public string? Doi { get; set;}
        public int? GenreId { get; set; }
        public Genres Genre { get; set; }
        public string? Pdf { get; set; }

    }
}
