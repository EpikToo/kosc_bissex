import { ComponentFixture, TestBed } from '@angular/core/testing';
import { BissexBannerComponent } from './bissex-banner.component';

describe('BissexBannerComponent', () => {
  let component: BissexBannerComponent;
  let fixture: ComponentFixture<BissexBannerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ BissexBannerComponent ]
    })
    .compileComponents();
    fixture = TestBed.createComponent(BissexBannerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
