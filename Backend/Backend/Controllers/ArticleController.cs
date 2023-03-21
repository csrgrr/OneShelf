using Backend.Config;
using Backend.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Backend.Controllers
{
    public class ArticleController : Controller
    {
        private readonly DBArticlesContext _context;
        public ArticleController(DBArticlesContext context) 
        { 
            _context = context;
        }


        //R
        [HttpGet("list")]
        public async Task<ActionResult<List<Article>>> Get()
        {
            return await _context.Articles.ToListAsync();
        }


        //C
        [HttpPost("save")]
        public async Task<ActionResult> Post(Article article)
        {
            _context.Add(article); //add to context
            await _context.SaveChangesAsync();

            return Ok();
        }

    }
}
