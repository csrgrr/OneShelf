using Backend.Config;
using Backend.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Backend.Controllers
{
    [Route("/api/article")]
    public class ArticleController : Controller
    {
        private readonly DBArticlesContext _context;
        public ArticleController(DBArticlesContext context) 
        { 
            _context = context;
        }


        //C
        [HttpPost("save")]
        public async Task<ActionResult> Post([FromBody]Article article)
        {
            _context.Add(article); //add to context
            await _context.SaveChangesAsync();

            return Ok(article);
        }

        //R
        [HttpGet("list")]
        public async Task<ActionResult<List<Article>>> GetArticles()
        {
            return await _context.Articles.Include(x => x.Genre).ToListAsync();
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Article>> ShowArticleById(int id)
        {
            var articleExist = await _context.Articles.AnyAsync(x => x.Id == id);

            if (!articleExist)
            {
                return BadRequest($"The article with id {id} does not exist");
            }

            return await _context.Articles.Include(x=>x.Genre).FirstOrDefaultAsync(x => x.Id == id);
        }


        //U
        [HttpPut("/updateArticle/{id}")]
        public async Task<ActionResult> Put(int id, Article article)
        {
            _context.Entry(article).State = EntityState.Modified;
            await _context.SaveChangesAsync();

            return Ok(article);
        }

        //D
        [HttpDelete("/deleteArticle/{id}")]
        public async Task<ActionResult> Delete(int id)
        {
            Article article = await _context.Articles.FindAsync(id);

            _context.Remove(article);

            await _context.SaveChangesAsync();
            
            return NoContent();
        }

    }
}
