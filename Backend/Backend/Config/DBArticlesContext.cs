using Backend.Models;
using Microsoft.EntityFrameworkCore;

namespace Backend.Config
{
    public class DBArticlesContext : DbContext
    {
        public DBArticlesContext(DbContextOptions<DBArticlesContext> options) : base(options)
        {

        }

        public DbSet<Article> Articles { get; set; }
        public DbSet<Genres> Genres { get; set; }
    }
}
