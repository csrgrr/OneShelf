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
        public async Task<ActionResult> Post(Article article)
        {
            _context.Add(article); //add to context
            await _context.SaveChangesAsync();

            return Ok(article);
        }

        //R
        [HttpGet("list")]
        public async Task<ActionResult<List<Article>>> Get()
        {
            return await _context.Articles.ToListAsync();
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Article>> Show(int id)
        {
            var article = await _context.Articles.FindAsync(id);
            return Ok(article);
        }


        //U
        [HttpPut("/update/{id}")]
        public async Task<ActionResult> Put(int id, Article article)
        {
            _context.Entry(article).State = EntityState.Modified;
            await _context.SaveChangesAsync();

            return Ok(article);
        }

        //D
        [HttpDelete("/delete/{id}")]
        public async Task<ActionResult> Delete(int id)
        {
            Article article = await _context.Articles.FindAsync(id);

            _context.Remove(article);

            await _context.SaveChangesAsync();
            
            return NoContent();
        }

    }
}
